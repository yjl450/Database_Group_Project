# -*- coding: UTF-8 -*- #
# Author: Zander_M
# Time: April, 25, 2019
# Title: User Blueprint 

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from AMS.db import get_db

bp = Blueprint('user',__name__)