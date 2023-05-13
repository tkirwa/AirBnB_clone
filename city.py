#!/usr/bin/python3
"""
City Class inheriting from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defining public class attributes
    """
    state_id = ""
    name = ""
