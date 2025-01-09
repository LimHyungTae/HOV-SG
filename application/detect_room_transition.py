import os
import hydra
from omegaconf import DictConfig
from hovsg.graph.graph import Graph

# pylint: disable=all


@hydra.main(version_base=None, config_path="../config", config_name="create_graph")
def main(params: DictConfig):
    # create logging directory
    save_dir = os.path.join(params.main.save_path, params.main.dataset, params.main.scene_id)
    params.main.save_path = save_dir
    params.main.dataset_path = os.path.join(params.main.dataset_path, params.main.split, params.main.scene_id)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    text_prompts = ["This image shows a transition between rooms.", 
                    "This image is taken inside a single room.",
                    "This image captures a clear transition between two distinct rooms. The foreground features an open doorway, hallway, or architectural boundary leading from one room to another.", 
                    "This image shows the interior of a single room, characterized by consistent furniture, decoration, and lighting without visible transitions or boundaries to other rooms.", 
                    "This image shows the boundary between two rooms, with contrasting elements such as flooring, walls, or lighting on either side.",
                    "This image captures a confined, self-contained space with uniform materials and decorations, providing no signs of adjacent areas.",
                    # for bed room detection
                    "This image shows a small, confined bathroom with limited space. The room contains compact fixtures such as a toilet, sink, and possibly a shower, with minimal floor area and walls close to each other.",
                    "This image depicts a narrow bathroom, characterized by tight spacing, small fixtures, and little room for movement. The walls, sink, and toilet are positioned close together.",
                    "This is a small restroom with basic fixtures like a sink and toilet, surrounded by plain tiles and cramped walls. The layout feels compact and enclosed.",
                    "The bathroom in this image feels confined and restricted, with limited walking space and closely positioned objects such as a sink, toilet, and possibly a narrow shower.",
                    "This image does not depict a spacious bathroom; instead, it captures a small and compact restroom with limited room for movement.",
                    # Open-plan structure
                    "This image shows two adjacent rooms separated by an open wall or archway. The spaces are functionally distinct but connected without a physical door.",
                    "This image depicts a transition between two rooms, divided by an open wall or structural boundary, with different flooring or furniture arrangements hinting at distinct functions.",
                    "This scene represents two connected spaces where no doors or full walls exist. The separation is implied through a partial wall or arch-like opening.",
                    "This image illustrates an open layout with two functionally distinct areas, such as a living room and dining room, divided by an open passage or decorative elements.",
                    "This image captures a transition in an open-plan design where two rooms are divided by a partial wall, column, or boundary, creating connected yet distinct spaces.",
                    # Narrow corridor
                    "This image shows a narrow hallway with limited walking space, where the walls are close together and the path feels confined and enclosed.",
                    "This image captures a small, tight corridor with walls on either side, leading to another part of the building. The space is linear and feels restrictive.",
                    "This is a narrow indoor hallway, characterized by its straight path, closely spaced walls, and minimal decor. The passage feels compact and functional.",
                    "This image depicts a narrow indoor passageway with limited space for movement. The corridor connects two areas and feels tightly enclosed by walls.",
                    "This image illustrates a cramped hallway where the walls on both sides are visible in close proximity, creating a sense of spatial restriction.",
                    "This narrow corridor connects two rooms and is defined by its tight dimensions, with walls and flooring leading the way through the space."
                    ]


    # create graph
    hovsg = Graph(params)
    hovsg.detect_room_transition(save_dir, text_prompts)

if __name__ == "__main__":
    main()
