from dispatch_sys.models import DegreeProgram
from dispatch_sys.serializers.degree_program_serializers import DegreeProgramSerializer


def degree_program_add_service(sender, data, callback, **kwargs):
    serializer = DegreeProgramSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({
            "success": True,
            "message": serializer.data
        })

    return callback({
        "success": False,
        "errors": serializer.errors
    })


def degree_program_all_service(sender, callback, **kwargs):
    degree_programs = DegreeProgram.objects.all()
    serializer = DegreeProgramSerializer(degree_programs, many=True)

    return callback({
        "success": True,
        "data": serializer.data
    })


def degree_program_show_service(sender, callback, pk, **kwargs):
    try:
        degree_program = DegreeProgram.objects.get(pk=pk)
        serializer = DegreeProgramSerializer(instance=degree_program)

        return callback({
            "success": True,
            "data": serializer.data
        })

    except DegreeProgram.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Degree Program does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def degree_program_update_service(sender, data, callback, pk, **kwargs):
    try:
        degree_program = DegreeProgram.objects.get(pk=pk)
        serializer = DegreeProgramSerializer(
            instance=degree_program,
            data=data,
            partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

    except DegreeProgram.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Degree Program not found"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def degree_program_delete_service(sender, callback, pk, **kwargs):
    try:
        degree_program = DegreeProgram.objects.get(pk=pk)

        # Serialize before deletion
        serializer = DegreeProgramSerializer(instance=degree_program)
        deleted_data = serializer.data

        degree_program.delete()

        return callback({
            "success": True,
            "message": f"Degree Program with id {pk} has been deleted",
            "data": deleted_data
        })

    except DegreeProgram.DoesNotExist:
        return callback({
            "success": False,
            "errors": f"Degree Program with id {pk} does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })
