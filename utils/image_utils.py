def is_image_file(filename: str) -> bool:
    return filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
