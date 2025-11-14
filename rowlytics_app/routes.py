"""Public-facing routes for the Rowlytics marketing site."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from flask import Blueprint, abort, render_template

public_bp = Blueprint("public", __name__)


@dataclass(frozen=True)
class TemplateCard:
    slug: str
    title: str
    blurb: str
    image_path: str
    template_name: str


TEMPLATE_CARDS: tuple[TemplateCard, ...] = (
    TemplateCard(
        slug="capture-workout",
        title="Capture Workout",
        blurb="Record your workout and get feedback live.",
        image_path="images/camera_cool.png",
        template_name="capture_workout.html",
    ),
    TemplateCard(
        slug="snapshot-library",
        title="Snapshot Library",
        blurb="View important moments captured during workouts.",
        image_path="images/snapshot_cool.png",
        template_name="snapshot_library.html",
    ),
    TemplateCard(
        slug="workout-summaries",
        title="Workout Summaries",
        blurb="View summaries and analytics from previous workouts.",
        image_path="images/folder_cool.png",
        template_name="workout_summaries.html",
    ),
    TemplateCard(
        slug="team-view",
        title="Team View",
        blurb="Join a team of like minded athletes and track collective progress.",
        image_path="images/team_cool.png",
        template_name="team_view.html",
    ),
)


def _iter_cards() -> Iterable[TemplateCard]:
    return iter(TEMPLATE_CARDS)


def _get_card(slug: str) -> TemplateCard | None:
    return next((card for card in TEMPLATE_CARDS if card.slug == slug), None)


@public_bp.route("/")
def landing_page() -> str:
    return render_template(
        "index.html",
        cards=_iter_cards(),
    )


@public_bp.route("/templates/<slug>")
def template_detail(slug: str) -> str:
    card = _get_card(slug)
    if card is None:
        abort(404)
    return render_template(card.template_name, card=card)