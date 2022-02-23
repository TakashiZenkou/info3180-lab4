from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images',IMAGES)

class UploadForm(FlaskForm):
    photo = FileField('Test',validators=[FileRequired(), FileAllowed(images,'Images only!')])