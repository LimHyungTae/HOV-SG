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

    # create graph
    hovsg = Graph(params)
    hovsg.create_pcd_map(os.path.join(save_dir, "full_pcd.ply")) 
    print("segmenting floors...")
    hovsg.segment_floors(save_dir)

    print("segmenting rooms...")
    for floor in hovsg.floors:
        hovsg.segment_rooms(floor, save_dir)

if __name__ == "__main__":
    main()
