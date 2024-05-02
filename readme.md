# Inventory Management App

This is an inventory management application built with FastAPI and SQLAlchemy.

## Description

The inventory management app allows users to perform CRUD operations on items in the inventory. It provides endpoints for creating, reading, updating, and deleting items, as well as uploading images for items.

## Features

- **Create Item**: Add a new item to the inventory.
- **Read Item**: Retrieve information about a specific item.
- **Update Item**: Modify the details of an existing item.
- **Delete Item**: Remove an item from the inventory.
- **Upload Image**: Upload an image for an item.

# Inventory App with FastAPI

This is a simple inventory management application built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. The application uses SQLAlchemy as an ORM for database operations.

## Prerequisites

-   Python 3.6+
-   FastAPI
-   Uvicorn (ASGI server)
-   SQLAlchemy
-   Pydantic

## Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required packages using pip

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload