class Settings:
    def __init__(self):
        self.screen_width = 1440
        self.screen_height = 720
        self.bg_color = (1, 0, 0)
        self.mario_lives = 3
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.high_score = 0
        self.frame = 0
        self.frame_end = 20
        self.level = 1
        self.time = 400
        self.time_count = 0
        self.coins = 0

    def get_frame(self):
        return self.frame

    def reset_scores(self, scores):
        self.time = 400
        self.coins = 0
        self.level = 1
        self.high_score = 0
        scores.prep_coins()
        scores.prep_lives()
        scores.prep_score()
        scores.prep_time()
        scores.prep_level()

    def update_time(self):
        self.time_count += 1
        if self.time_count > 40 and self.time != 0:
            self.time_count = 0
            self.time -= 1
