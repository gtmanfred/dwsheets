from enum import Enum
from typing import Annotated
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import Field


class BaseTag(BaseModel):
    type: str
    text: str


class Quantity(BaseTag):
    type: Literal['quantity']
    modifier: int
    text: str = 'The amount of this object that a person has.'


class Applied(BaseTag):
    type: Literal['applied']
    text: str = "It’s only useful when carefully applied to a person or to something they eat or drink."


class Awkward(BaseTag):
    type: Literal['awkward']
    text: str = "It’s unwieldy and tough to use."


class DurationEnum(str, Enum):
    ongoing: str = 'ongoing'
    forward: str = 'forward'


class Bonus(BaseTag):
    type: Literal['bonus']
    modifier: int
    options: DurationEnum
    text: str = (
        'It modifies your effectiveness in a specified situation. '
        'It might be “+1 forward to spout lore” or “-1 ongoing to hack and slash.”'
    )


class Coins(BaseTag):
    type: Literal['coins']
    modifier: int
    text: str = (
        "How much it costs to buy, normally. If the cost includes “-Charisma” "
        "a little negotiation subtracts the haggler’s Charisma score (not modifier) from the price."
    )


class Dangerous(BaseTag):
    type: Literal['dangerous']
    text: str = (
        "It’s easy to get in trouble with it. If you interact with it without proper "
        "precautions the GM may freely invoke the consequences of your foolish actions."
    )


class Ration(BaseTag):
    type: Literal['ration']
    text: str = "It's edible, more or less"


class Requires(BaseTag):
    type: Literal['requires']
    modifier: str
    text: str = "It’s only useful to certain people. If you don’t meet the requirements it works poorly, if at all."


class Slow(BaseTag):
    type: Literal['slow']
    text: str = 'It takes minutes or more to use.'


class Touch(BaseTag):
    type: Literal['touch']
    text: str = "It’s used by touching it to the target’s skin."


class TwoHanded(BaseTag):
    type: Literal['two-handed']
    text: str = 'It takes two hands to use it effectively.'


class Weight(BaseTag):
    type: Literal['weight']
    modifier: int
    text: str = (
        "Count the listed amount against your load. "
        "Something with no listed weight isn’t designed to be carried. "
        "100 coins in standard denominations is 1 weight. "
        "The same value in gems or fine art may be lighter or heavier."
    )


class Worn(BaseTag):
    type: Literal['worn']
    text: str = "To use it, you have to be wearing it."


class Uses(BaseTag):
    type: Literal['uses']
    modifier: int
    text: str = "It can only be used n times."


class Hand(BaseTag):
    type: Literal['hand']
    text: str = "It’s useful for attacking something within your reach, no further."


class Armor(BaseTag):
    type: Literal['armor']
    modifier: int
    text: str = (
        "It protects you from harm and absorbs damage. "
        "When you take damage, subtract your armor from the total. "
        "If you have more than one item with n Armor, only the highest value counts."
    )


class ArmorModifier(BaseTag):
    type: Literal['armor_modifier']
    modifier: int
    text: str = "It protects you and stacks with other armor. Add its value to your total armor."


class Close(BaseTag):
    type: Literal['close']
    text: str = "It’s useful for attacking something at arm’s reach plus a foot or two."


class Damage(BaseTag):
    type: Literal['damage']
    modifier: int
    text: str = "It is particularly harmful to your enemies. When you deal damage, you add n to it."


class Clumsy(BaseTag):
    type: Literal['clumsy']
    modifier: int
    text: str = 'It’s tough to move around with. -1 ongoing while using it. This penalty is cumulative.'


class Ammo(BaseTag):
    type: Literal['ammo']
    modifier: int
    text: str = (
        'It counts as ammunition for appropriate ranged weapons. '
        'The number indicated does not represent individual arrows or sling stones, '
        'but represents what you have left on hand.'
    )


class Forceful(BaseTag):
    type: Literal['forceful']
    text: str = 'It can knock someone back a pace, maybe even off their feet.'


class IgnoresArmor(BaseTag):
    type: Literal['ignores-armor']
    text: str = "Don't subtract armor from the damage taken."


class Messy(BaseTag):
    type: Literal['messy']
    text: str = 'It does damage in a particularly destructive way, ripping people and things apart.'


class Piercing(BaseTag):
    type: Literal['piercing']
    modifier: int
    text: str = (
        "It goes right through armor. When you deal damage with n piercing, "
        "you subtract n from the enemy’s armor for that attack."
    )


class Precise(BaseTag):
    type: Literal['precise']
    text: str = "It rewards careful strikes. You use DEX to hack and slash with this weapon, not STR."


class Reload(BaseTag):
    type: Literal['reload']
    text: str = "After you attack with it, it takes more than a moment to reset for another attack."


class Stun(BaseTag):
    type: Literal['stun']
    text: str = "When you attack with it, it does stun damage instead of normal damage."


class Thrown(BaseTag):
    type: Literal['thrown']
    text: str = (
        "Throw it at someone to hurt them. "
        "If you volley with this weapon, you can’t choose to mark off ammo on a 7–9; "
        "once you throw it, it’s gone until you can recover it."
    )


class Reach(BaseTag):
    type: Literal['reach']
    text: str = "It’s useful for attacking something that’s several feet away—maybe as far as ten."


class Near(BaseTag):
    type: Literal['near']
    text: str = "It’s useful for attacking if you can see the whites of their eyes."


class Far(BaseTag):
    type: Literal['far']
    text: str = "It’s useful for attacking something in shouting distance."


Tag = Annotated[Union[tuple(BaseTag.__subclasses__())], Field(discriminator='type')]
