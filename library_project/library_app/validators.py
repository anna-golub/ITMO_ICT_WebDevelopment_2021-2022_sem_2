from django.core.exceptions import ValidationError
import magic


def validate_file_size(file_upload):
    limit = 200 * 1024 * 1024  # 200 MiB
    # limit = 2 * 1024  # 2 KB

    if file_upload.size > limit:
        raise ValidationError('The file is too large. File size limit is %d.' % limit)


def validate_file_type(file_upload):
    possible_extensions = ('image/png', 'image/jpeg',
                           'text/plain',  # .txt
                           'text/x-python',  # .py
                           )

    content_type = magic.from_buffer(file_upload.read(), mime=True)
    if content_type not in possible_extensions:
        raise ValidationError('Files of type %s are not supported.' % content_type)
