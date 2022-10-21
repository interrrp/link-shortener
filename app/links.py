import http
import secrets

import pydantic
from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse

router = APIRouter()


class Link(pydantic.BaseModel):
    id: str  # 6 character ID
    url: pydantic.HttpUrl  # Unshortened URL


class LinkInput(pydantic.BaseModel):
    url: pydantic.HttpUrl  # Unshortened URL


links: list[Link] = []


@router.get("/{link_id}")
async def get_link(link_id: str, response: Response) -> RedirectResponse | dict:
    """Redirect to the URL for a link ID."""

    try:
        # Search for the link with the ID
        link = [link for link in links if link.id == link_id][0]

        return RedirectResponse(link.url)
    except IndexError:
        # If the link ID doesn't exist, return a 404
        response.status_code = http.HTTPStatus.NOT_FOUND
        return {"error": "Link not found"}


@router.post("/")
async def shorten_link(link: LinkInput) -> Link:
    """Shorten a link."""

    # Check if this link already exists
    if link.url in [link.url for link in links]:
        # Just return the existing link ID
        return [link for link in links if link.url == link.url][0]

    new_link = Link(
        id=secrets.token_urlsafe(6),  # Generate a short 6 character ID for the link
        url=link.url,
    )

    links.append(new_link)

    return new_link
