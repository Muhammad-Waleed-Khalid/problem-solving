def is_rectangle_overlap(rec1, rec2):
  
  x_rec1 = rec1[0]<rec2[2]
  y_rec1 = rec1[1]<rec2[3]

  x_rec2 = rec2[0]<rec1[2]
  y_rec2 = rec2[1]<rec1[3]
  return x_rec1 and x_rec2 and y_rec1 and y_rec2

def main():
  rec1_input_lists = [[0,0,2,2], [0,0,1,1], [0,0,1,1], [0,0,2,2], [1,1,2,2]]
  rec2_input_lists = [[1,1,3,3], [1,0,2,1], [2,2,3,3], [0,0,2,2], [3,3,6,6]]

  for i in range(len(rec1_input_lists)):
    result = is_rectangle_overlap(rec1_input_lists[i], rec2_input_lists[i])
    print(str(i+1) + ". is_rectangle_overlap (" + str(rec1_input_lists[i]) + "," + str(rec2_input_lists[i]) + "): " + str(result))
    print("-------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()