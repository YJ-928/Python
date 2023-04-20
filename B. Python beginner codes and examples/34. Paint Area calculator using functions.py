def Calculate(height_of_wall, width_of_wall, can_coverage=5):
    Cans_req = round((height_of_wall*width_of_wall)/can_coverage)
    return print(f"\nYou will require {Cans_req} Cans of Paint\n")


Calculate(height_of_wall=float(input("\nEnter height of wall: ")),
          width_of_wall=float(input("\nEnter width of wall: ")))
