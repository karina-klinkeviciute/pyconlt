from ckeditor.fields import RichTextField
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CommitteeMember(models.Model):
    """Extended basic django user model."""

    # This field is required
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    bio = RichTextField(help_text=_("Committee member bio"), blank=True, null=True)

    committee = models.ForeignKey("committee.Committee", on_delete=models.CASCADE)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        """Overridden save method in order to save CommitteeMember's User account to a new permission group."""
        committee_members_group, created_group = Group.objects.get_or_create(name="committee_members")
        content_type = ContentType.objects.get_for_model(Group)
        committee_member_permissions, created_permissions = Permission.objects.get_or_create(
            codename="is_committee_member",
            name="is_committee_member",
            content_type=content_type,
        )
        if created_group:
            committee_members_group.permissions.add(committee_member_permissions)
        super(CommitteeMember, self).save(*args, **kwargs)
        self.user.user_permissions.add(committee_member_permissions)
        self.user.groups.add(committee_members_group)

    def delete(self, *args, **kwargs):
        """Overridden delete method in order to remove CommitteeMember's User account from permission group."""
        committee_member_permissions = Permission.objects.filter(
            codename="is_committee_member",
            name="is_committee_member",
        ).first()
        committee_members_group = Group.objects.filter(name="committee_members").first()
        self.user.user_permissions.remove(committee_member_permissions)
        self.user.groups.remove(committee_members_group)
        super(CommitteeMember, self).delete(*args, **kwargs)
