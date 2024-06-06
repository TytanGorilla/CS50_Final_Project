from tabulate import tabulate
import cowsay # type: ignore

class Body:
    #class variables
    _parts = {
        "neck": {
                "anterior": ["sternocleidomastoid"],
                "lateral": ["scalene"],
                "posterior": ["trapezius"]
                },
        "shoulders": {
                "anterior": ["anterior deltoid"],
                "lateral": ["lateral deltoid"],
                "posterior": ["posterior deltoid"]
                },
        "arms": {
                "upper": ["biceps", "brachialis", "triceps"],
                "lower": ["forearms"]
                },
        "chest": {
                "upper": ["clavicular"],
                "lower": ["sternal"]
                },
        "back": {
                "upper": ["rhomboids"],
                "mid": ["erector spinae"],
                "lower": ["latissimus dorsi"]
                },
        "abs": {
                "upper": ["serratus anterior", "rectus abdominis"],
                "lower": ["transverse abdominis", "oblique"]
                },
        "legs": {
                "upper": ["glutes", "hamstrings", "quadriceps"],
                "lower": ["calves", "tibialis anterior"]
                },
        "cardio": {
                "low_intensity": ["walking", "cycling", "rowing"],
                "high_intensity": ["running", "sprinting", "cycling", "rowing"]
                },
        "conditioning": {
                "weight_gain": ["caloric surplus"],
                "weight_loss": ["caloric deficit"]
                }
    }
    @classmethod
    def list_parts(cls):
        return list(cls._parts.keys())


def main():
    training_priority = greet_obj()
    more_specific = specify(training_priority)
    target(more_specific)


def greet_obj() -> object:
    body_parts = []
    for index, key in enumerate(Body._parts):
        body_parts.append([key.capitalize(), index+1])

    cowsay.trex(f"RAWWWWWWR! Good day!\n Looking train, but don't know where to start?\n Pick a number from the table below: ")
    print(tabulate(body_parts, headers=["Body Parts", "Select No."], tablefmt="grid", numalign="center", stralign="center"))

    while True:
        prioriT = input(f"\nIf you could improve one aspect of your body, what would it be?\nInput a number to establish your training priority: ")
        try:
            priority = int(prioriT)
            for part in body_parts:
                if part[1] == int(priority):
                    return part[0] # ['Chest', 4] -> Chest

        except ValueError:
             raise ValueError("Input an INT!")


def specify(priority) -> list: # Chest
    part = priority.lower()
    mod_list = Body._parts[part]
    body_parts = []
    for index, key in enumerate(mod_list):
        body_parts.append(f"{key.capitalize()} {part} Select: {index+1}")

    print(f"\n{tabulate(mod_list, headers=body_parts, tablefmt="grid")}")
    while True:
        try:
            be_specific = input(f"\nWhat part of {part} do you wish to specialize?\nPlease input appropriate number: ")
            for ind, ki in enumerate(mod_list):
                if (ind+1) == int(be_specific):
                    cowsay.kitty(f"Specializing in {ki} {part}.")
                    return [part, ki]

        except ValueError:
            raise ValueError("Input the appropriate number from the table!")


def target(specific) -> object:
    aim, key = specific
    focus = Body._parts[aim][key]
    indexed_focus = []

    for index, k in enumerate(focus):
        indexed_focus.append([index+1, k.capitalize()])

    print(tabulate(indexed_focus, headers=["Select No.", "Muscle Group"], tablefmt="grid"))

    while True:
        try:
            targeted = input(f"\nTo achieve your aim of targeting the {key} {aim}.\nPlease select select what will become your focus from the table above!\nInput: ")
            for i in indexed_focus:
                if i[0] == int(targeted):
                    cowsay.cheese(f"Let's focus on your,\n{i[1].lower()} region of your {aim}.")
                    return i[1]

        except ValueError:
            raise ValueError("Again, input a number in the 'Select No.' column!")


if __name__ == "__main__":
    main()
