import docutils.nodes as nodes


class RatingContainer(nodes.container):
    tagname = "span"


def rating_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    A screen-reader accessible difficulty rating.
    """
    aria_label = f"difficulty rating:{text} out of 5"
    content =f"{"★"*int(text): ☆<5}
    
    node = RatingContainer(content)
    node["role"] = "image"
    node["aria-label"] = aria_label

    return [node]


def setup(app):
    """
    Install the plugin.
    """
    app.add_role('rating', rating_role)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
