"""
Job Organizer - Minimal Reflex App for Render Deployment Testing
This is a minimal version to ensure deployment works correctly
"""
import reflex as rx

class State(rx.State):
    """Simple state for testing"""
    message: str = "Backend connected successfully! ✅"
    counter: int = 0
    
    def increment(self):
        """Test state mutation"""
        self.counter += 1
        self.message = f"Button clicked {self.counter} times"

def index() -> rx.Component:
    """Minimal page to test deployment"""
    return rx.container(
        rx.vstack(
            rx.heading("Job Organizer - Minimal Test", size="9"),
            rx.text(
                "Testing Render Deployment",
                size="5",
                color="gray"
            ),
            rx.divider(),
            rx.card(
                rx.vstack(
                    rx.heading("Connection Status", size="6"),
                    rx.text(State.message, size="4", color="green"),
                    rx.button(
                        "Test Backend Connection",
                        on_click=State.increment,
                        size="3",
                        color_scheme="blue"
                    ),
                    spacing="4",
                ),
                width="100%",
            ),
            rx.text(
                "If you can see this page and the button works, deployment is successful!",
                size="2",
                color="gray",
                margin_top="4"
            ),
            spacing="6",
            padding="4",
            max_width="800px",
        ),
        center_content=True,
        height="100vh",
    )

# Create the app
app = rx.App()
app.add_page(index, route="/", title="Job Organizer - Test")
