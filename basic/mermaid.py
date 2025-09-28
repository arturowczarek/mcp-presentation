def render_mermaid(mermaid_code: str, output_file: str = "diagram.png"):
    """Render a Mermaid diagram to display it in Jupyter Notebook."""
    from langchain_core.runnables.graph_mermaid import draw_mermaid_png
    draw_mermaid_png(mermaid_syntax=mermaid_code, output_file_path=output_file)
    from IPython.display import Image
    return Image(output_file)

def display_mermaidd(mermaid_code: str):
    """Display the Mermaid diagram in Jupyter Notebook."""
    display(render_mermaid(mermaid_code))