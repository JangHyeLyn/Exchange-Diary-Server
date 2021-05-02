from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountRegisterAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        sociallogin.save(request)
        return user
