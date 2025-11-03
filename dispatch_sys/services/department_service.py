from dispatch_sys.models import Department
from dispatch_sys.serializers.department_serializers import DepartmentSerializer


def department_add_service(sender, data, callback, **kwargs):
    serializer = DepartmentSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        callback(
            {
                "success": True,
                "message": serializer.data
            }
        )

    return callback(
        {
            "success": False,
            "errors": serializer.errors
        }
    )


def department_all_service(sender, callback, **kwargs):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)

    return callback(
        {
            "success": True,
            "data": serializer.data
        }
    )


def department_delete_service(sender, callback, pk, **kwargs):
    try:
        department = Department.objects.get(pk=pk)

        # serialize data before deletion to return it
        serializer = DepartmentSerializer(instance=department)
        deleted_data = serializer.data

        # Delete the object
        department.delete()

        return callback({
            "success": True,
            "message": f"Department with id {pk} has been deleted",
            "data": deleted_data
        })

    except Department.DoesNotExist:
        return callback({
            "success": False,
            "errors": f"Department with id {pk} does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def department_show_service(sender, callback, pk, **kwargs):
    try:
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(instance=department)
        return callback({
            "success": True,
            "data": serializer.data
        })

    except Department.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Department does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def department_update_service(sender, data, callback, pk, **kwargs):
    try:
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(instance=department, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

    except Department.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Department not found"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })
