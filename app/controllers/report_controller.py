from fastapi import APIRouter
from fastapi.responses import Response

from app.domain.schemas import DateRangeRequest
from app.domain.services import generate_pdf, render_report_html

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/pdf")
async def generate_report_pdf(body: DateRangeRequest) -> Response:
    html = render_report_html(body.start_date, body.end_date)
    pdf_bytes = generate_pdf(html)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=relatorio.pdf"},
    )
