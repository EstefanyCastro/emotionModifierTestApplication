from tkinter import Toplevel, Label


class TooltipManager:
    def __init__(self, widget):
        self.widget = widget

    def show_tooltip(self, event, message):
        x, y, _, _ = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 25

        # Show the tooltip
        self.tooltip = Toplevel(event.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        Label(
            self.tooltip,
            text=message,
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
        ).pack()

    def hide_tooltip(self, event):
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()
