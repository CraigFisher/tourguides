from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.utils.decorators import method_decorator
from profiles.forms import MemberProfileForm, GuideProfileForm, UserForm
from profiles.models import MemberProfile, GuideProfile


def create(request):
    pass


class Profile(View):

    def get(self, request, user_id):
        profile_owner = User.objects.get(pk=user_id)
        requester_is_owner = str(request.user.id) == user_id
        owner_is_guide = hasattr(profile_owner, "guideprofile")

        if not requester_is_owner and not owner_is_guide:
            raise PermissionDenied

        context = {'profile_owner': profile_owner}
        if owner_is_guide:
            context['guide'] = True
            context['profile'] = profile_owner.guideprofile
        else:
            context['profile'] = profile_owner.memberprofile

        if not requester_is_owner or request.GET.get("preview") == 1:
            return render(request, 'profiles/public_profile.html', context)
        else:  # Present owner with their edit page
            userForm = UserForm(instance=profile_owner, prefix='user')
            if owner_is_guide:
                profileForm = GuideProfileForm(instance=profile_owner.guideprofile)
            else:
                profileForm = MemberProfileForm(instance=profile_owner.memberprofile)
            context['userForm'] = userForm
            context['profileForm'] = profileForm
            return render(request, 'profiles/profile_editor.html', context)

    def post(self, request):
        pass

    @method_decorator(login_required)
    def dispatch(self, request, user_id):
        return super(Profile, self).dispatch(request, user_id)
