from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):

        if request.method == 'GET':
            return True  # Allow GET requests without authentication
        # Custom authentication logic here
        return super().is_authenticated(request, **kwargs)