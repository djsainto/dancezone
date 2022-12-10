from flask import Blueprint, request, render_template

from app.dance import fetch_unemployment_data, format_pct
