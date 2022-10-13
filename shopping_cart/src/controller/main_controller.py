from fastapi import APIRouter
from fastapi.responses import HTMLResponse


MAIN_ROUTE = APIRouter(prefix="/magaluJA")


@MAIN_ROUTE.get("/", response_class=HTMLResponse)
async def welcome_page():
    html = """
        <h2>Grupo 11 - Code, Mesa e Banho</h2>

        <p><strong>Fernanda Spineli </strong>&middot; <a href="https://github.com/FernandaSpineli">GitHub</a>&nbsp;&middot; LinkedIn</p>

        <p><strong>Karoline Lemos&nbsp;</strong>&middot; <a href="https://github.com/karolinelemos">GitHub</a>&nbsp;&middot; LinkedIn</p>

        <p><strong>Mariana Faria&nbsp;</strong>&middot; <a href="https://github.com/marianaicf">GitHub</a>&nbsp;&middot; LinkedIn</p>

        <p><strong>Poliana Frenhan&nbsp;</strong>&middot;&nbsp;<a href="https://github.com/polifrenhan">GitHub</a>&nbsp;&middot; <a href="http://www.linkedin.com/in/polifrenhan/">LinkedIn</a></p>

        <p><strong>Taila Musardo&nbsp;</strong>&middot; <a href="https://github.com/tailamusardo">GitHub</a>&nbsp;&middot; LinkedIn</p>

        <p><span style="font-family:times new roman,times,serif"><span style="font-size:10px"><em>Participa&ccedil;&otilde;es especiais: Alice e</em></span><span style="font-size:9px"><em> Joana&nbsp;</em><img alt="heart" height="23" src="https://clevert.com.br/lib/ckeditor/plugins/smiley/images/heart.png" title="heart" width="23" /></span></span></p>

        <address><img alt="" height="300" src="https://cf.shopee.com.br/file/df519fc7e2b6f5d78444422242af4cf5" width="300" />
        <p>&nbsp;</p>
        </address>
        """

    return html


@MAIN_ROUTE.get("/agradecimentos/", response_class=HTMLResponse)
async def acknowledgement_page():
    html = """
    <h2>Grupo 11 - Code, Mesa e Banho</h2>
    """

    return html
