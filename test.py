import pyVSSSReferee



from pyVSSSReferee.RefereeComm import RefereeComm


r = RefereeComm(config_file = "config.json")
r.start()
while (True):
    if r.get_foul() == "KICKOFF":
        r.send_replacement([{"robot_id": 0, "x": -0.2, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.4, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.6, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "FREE_BALL":
        r.send_replacement([{"robot_id": 0, "x": 0, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.5, "y": -0.5, "orientation":0},
                            {"robot_id": 2, "x": 0.3, "y": 0.3, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "GOAL_KICK" and r.get_color() == 'BLUE':
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "GOAL_KICK" and r.get_color() == 'YELLOW':
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "PENALTY_KICK" and r.get_color() == "YELLOW":
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "PENALTY_KICK" and r.get_color() == "BLUE":
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "FREE_KICK" and r.get_color() == "YELLOW":
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    elif r.get_foul() == "FREE_KICK" and r.get_color() == "BLUE":
        r.send_replacement([{"robot_id": 0, "x": -0.5, "y": 0, "orientation":0},
                            {"robot_id": 1, "x": -0.3, "y": 0, "orientation":0},
                            {"robot_id": 2, "x": -0.1, "y": 0, "orientation":0}
                            ], "BLUE")
        
    