from rest_framework_simplejwt.tokens import RefreshToken


def user_logout_service(sender, callback, user=None, refresh_token=None, **kwargs):
    """
    Logs out a user by blacklisting the refresh token.
    """
    try:
        if not refresh_token:
            return callback({"success": False, "error": "Refresh token is required"})

        # Blacklist the refresh token
        token = RefreshToken(refresh_token)
        token.blacklist()  # requires rest_framework_simplejwt.token_blacklist app

        return callback({"success": True, "message": "Logged out successfully"})

    except Exception as e:
        return callback({"success": False, "error": str(e)})
