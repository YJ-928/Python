try:
   # creating individual rows as lists
    row1 = ["⬜️", "️⬜️", "️⬜️"]
    row2 = ["⬜️", "⬜️", "️⬜️"]
    row3 = ["⬜️️", "⬜️️", "⬜️️"]

    # creating a nested list as a matrix using above 3 row lists
    map = [row1, row2, row3]
    print(f"\n{row1}\n{row2}\n{row3}\n")

    # taking user inputs (column + Row,ie.. 32 == column 3 and row 2)
    position = input(
        "Where do you want to put the treasure? [Enter values between 00 - 22]  ")

    # inserting the position elements inside map
    map[int(position[:1])][int(position[1:])] = "X"

    # printing out Treasure marked spot with map
    print(
        f"\nYour Treasure Map is updated with your treasure position,Keep it safe!\n\n{row1}\n{row2}\n{row3}\n")

except IndexError as Err:
    print("\n❌ ❌ ERROR ❌ ❌\nOnly enter the values between [00 - 22]\n\n")
