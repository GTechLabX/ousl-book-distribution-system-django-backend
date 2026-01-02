


def test_service(sender, callback, **kwargs):
    return callback(
        {
            "success": True,
            "data": 'good'
        }
    )
