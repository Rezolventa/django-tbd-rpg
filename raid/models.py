from django.db import models


def empty_list():
    return {}


class Location(models.Model):
    """
    Основная идея: состояние противников и состояние лута шэрится между игроками, это вносит элемент MMO.

    Комментарий к метаданным.

    enemy_info - содержит данные о противниках, которые спавнятся на данной локации
    Пример:
    [
        {
            "enemies": {
                "id": 1,
                "quantity": 3
            },
            "respawn_cooldown": 60
        },
        ...
    ]

    enemy_state_info - содержит данные о состоянии противников
    Пример:
    [
        {
            "enemies": {
                "id": 1,
                "quantity": 1,
            },
            "respawn_datetime": <datetime>
        },
        ...
    ]

    loot_info - содержит данные о луте, который спавнится на данной локации
    Пример:
    [
        {
            "loot": [
                {
                    "quality": 1,
                    "quantity": 3
                },
            ]
            "respawn_cooldown": 60
        },
        ...
    ]

    loot_state_info - содержит данные о состоянии лута
    """
    name = models.CharField()
    description = models.CharField(null=True)
    enemy_info = models.JSONField(default=empty_list)
    enemy_state_info = models.JSONField(default=empty_list)
    loot_info = models.JSONField(default=empty_list)
    loot_state_info = models.JSONField(default=empty_list)
    image = models.ImageField(upload_to='static')
