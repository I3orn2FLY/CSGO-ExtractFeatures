import cv2
import json
import os
from config import SANDBOX_DATA


def draw_dead(img, x, y, r=10, color=(255, 255, 255), thickness=None):
    tl = (int(x - r), int(y - r))
    bl = (int(x - r), int(y + r))
    tr = (int(x + r), int(y - r))
    br = (int(x + r), int(y + r))
    cv2.line(img, tl, br, color, thickness)
    cv2.line(img, bl, tr, color, thickness)


if __name__ == "__main__":

    # Parse the demofile, output results to dictionary with df name as key
    data = json.load(open("entropiq-vs-sinners-mirage.json", "r"))

    rounds = data["gameRounds"]

    round_n = 3
    frames = rounds[round_n]["frames"]

    off_x = -3230
    off_y = 1713
    scale = 5

    img = cv2.imread(os.path.join(SANDBOX_DATA, "de_mirage_light.png"))

    fps = 5
    out = cv2.VideoWriter(f"mirage_round_{round_n}.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                          img.shape[:2][::-1])

    for frame in frames:
        draw = img.copy()
        clock = frame["clockTime"]
        cv2.putText(draw, clock, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        players = frame["t"]["players"] + frame["ct"]["players"]
        for p in players:
            x = (p["x"] - off_x) / scale
            y = (off_y - p["y"]) / scale
            x = int(x)
            y = int(y)

            color = (0, 255, 100) if p["side"] == "T" else (255, 150, 0)
            if p["isAlive"]:
                cv2.circle(draw, (x, y), 7, color, -1)
            else:
                draw_dead(draw, x, y, 5, color, 2)

        out.write(draw)
        cv2.imshow("Mirage", draw)
        cv2.waitKey(10)

    out.release()
