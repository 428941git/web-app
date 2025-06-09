from util.utils import get_frame, makeplot
from util.web import get_json
import io, base64

def cr_plot(start, end, code):
    plot = makeplot(get_frame(get_json("A", None, start, end), code))

    buf = io.BytesIO()
    plot.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')

    return img
def cr_table(start, end, code):
    table = get_frame(get_json("A", None, start, end), code)

    return table.to_dict(orient="records")
