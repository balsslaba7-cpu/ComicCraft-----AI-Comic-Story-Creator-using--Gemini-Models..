from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(request: Request,
                         story_prompt: str = Form(...),
                         character_name: str = Form(...),
                         setting: str = Form(...),
                         tone: str = Form(...),
                         art_style: str = Form(...)):
    outline = generate_outline(story_prompt)
    story = generate_story(outline)
    images = [generate_image(panel["image_prompt"]) for panel in outline]
    layout = build_comic_layout(outline, story, images)
    pdf_path = save_pdf(layout)

    return templates.TemplateResponse("comic_preview.html", {
        "request": request,
        "layout": layout,
        "pdf_path": pdf_path
    })

@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request):
    return templates.TemplateResponse("export_success.html", {"request": request})
