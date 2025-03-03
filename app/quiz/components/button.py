from django_components import component

@component.register("button")
class Button(component.Component):
    template_name = "components/question_card.html"

    def get_context_data(self, label="Kattints ide", color="primary"):
        return {"label": label, "color": color}
