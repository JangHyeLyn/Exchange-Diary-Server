from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountRegisterAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        sociallogin.save(request)
        return user

    #def populate_user(self, request, sociallogin, data):
    #    print(data)
    #    user = sociallogin.user
    #    return user

