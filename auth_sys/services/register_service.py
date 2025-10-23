from auth_sys.serializers.register_serializer import RegisterSerializer


def register_service(sender, data, callback, **kwargs):
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({
            'success': True,
            'message': 'User has been successfully register'
        })

    else:
        return callback({
            'success': False,
            'error': serializer.errors
        })
