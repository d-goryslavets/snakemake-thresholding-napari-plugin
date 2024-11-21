from typing import TYPE_CHECKING

from magicgui import magic_factory
from magicgui.widgets import CheckBox, Container, create_widget
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget
from skimage.util import img_as_float
import pathlib

from snakemake import snakemake

if TYPE_CHECKING:
    import napari

# Uses the `autogenerate: true` flag in the plugin manifest
# to indicate it should be wrapped as a magicgui to autogenerate
# a widget.
@magic_factory(
        call_button="Run",
)
def run_thres(
    workflow: pathlib.Path,
    params_yaml: pathlib.Path
) -> None:
    snakemake(
        workflow,
        configfiles = [
            params_yaml,
        ],
        use_conda = True,
        printshellcmds = True,
        keepgoing = True,
        latency_wait = 60
    )
    
