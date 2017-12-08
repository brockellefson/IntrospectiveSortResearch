/*
 * IntroSort.c
 * 432 algorithm project (introsort C optimization), 2017
 *
 * ---------------------------------------------------- Optimization ----------------------------------------------------
 *
 *  template <class RandomAccessIterator, class T, class Distance>
 *  void introsort_loop(RAI first, RAI last, T*, Distance depth_limit)
 *  {
 *      while (last - first > stl_threshold) {
 *          if (depth_limit == 0) {
 *              partial_sort(first, last, last);
 *              return;
 *          }
 *          depth_limit--;
 *          RAI cut = __unguarded_partition(first, last, T(__median(*first, *(first + (last - first) / 2), *(last - 1))));
 *          introsort_loop(cut, last, value_type(first), depth_limit);
 *          last = cut;
 *      }
 *  }
 *
 *-----------------------------------------------------------------------------------------------------------------------
 */


#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>


/* STL defines __stl_threshold as const int 16 */
#undef  SIZE_THRESHOLD
#define SIZE_THRESHOLD 16

/*************************************************************************************************************************/
/* Prototypes */
void introsort_loop(int first_index, int last_index, /* pointer???? */ int* array, int depth_limit); /* need to switch to C++ template */
int int_compare(int a, int b);
void swap(int* array, int first, int second);
int partition(int first_index, int last_index, int median, int* array);
int median(int first, int middle, int last, int* array); /* "__median" */
void insertionsort(int first, int last, int* array);
/************************************************************************************************************************/

/* Uncomment if using the STL C++ library
 template <class RandomAccessIterator, class T, class Distance>
 void introsort_loop(RandomAccessIterator first, RandomAccessIterator last, T*, Distance depth_limit)
 {
 while (last - first > stl_threshold) {
 if (depth_limit == 0) {
 partial_sort(first, last, last);
 return;
 }
 depth_limit--;
 RandomAccessIterator cut = __unguarded_partition(first,
 last,
 T(__median(*first,
 *(first + (last - first) / 2),
 *(last - 1))));
 introsort_loop(cut, last, value_type(first), depth_limit);
 last = cut;
 }
 }
 */

/************************************************************************************************************************/
/* Main */
int main(int argc, char* argv[])
{
    if (argc <= 1) {
        printf("Program only takes input size (of data structure) as argument\n");
        return 0;
    }
    
    int input_size = atoi(argv[1]);
    
    srand(time(NULL));
    
    /* variable initializations */
    struct timeval start_time, end_time, elapsed_time;
    
    FILE* file_p = fopen("introsort-c.csv", "a+");
    
    /* most important part of the algorithm */
    
    int number_of_tests;
    for (number_of_tests = 0; number_of_tests < 50; number_of_tests++) {
        long int average = 0;
        for (int i = 0; i < 25; i++) {
            int test_vector[input_size];
            /* initialize each test_vector of size 100, 500, 1000, etc. */
            for (int j = 0; j < input_size; j++) {
                test_vector[j] = rand() % (input_size - 1) + 1;
            }
            
            /* calculate floor */
            int floor = (int) (log(input_size - 0) / log(2));
            floor = 2 * floor;
            
            /* start timer */
            gettimeofday(&start_time, NULL);
            
            introsort_loop(0, input_size - 1, test_vector, floor);
            /* uncomment C++ STL library */
            /* introsort_loop(&test_vector[0], test_vector[input_size - 1], value_type(first), floor) */
            insertionsort(floor, input_size, test_vector);
            
            /* end timer */
            gettimeofday(&end_time, NULL);
            timersub(&end_time, &start_time, &elapsed_time);
            
            average += (long int) elapsed_time.tv_usec;
        }
        
        /* write to .csv file */
        fprintf(file_p, "%d, %ld\n", input_size, (long int) (average / 25));
        
    }
    
    fclose(file_p);
    
    /* print time */
    
    return 0;
}
/************************************************************************************************************************/


/************************************************************************************************************************/
/* bootstrapped C/C++ */
/* Function definitions */
void introsort_loop(int first_index, int last_index, /* pointer???? */ int* array, int depth_limit)
{
    /* while the size to sort > threshold */
    while (last_index - first_index > SIZE_THRESHOLD) {
        
        /* base case */
        if (depth_limit == 0) {
            heapsort(array, (depth_limit - 1), sizeof(int), (int(*)(const void*, const void*))int_compare); /* The C Unix equivalent of */
            return;                                                                                         /* STL __partial_sort */
        }
        
        depth_limit--;
        /* vvvvvv = __median if using the STL library */
        int median_value = median(first_index, (first_index + (last_index - first_index) / 2), (last_index - 1), array);
        
        int cut = partition(first_index, last_index, median_value, array);
        introsort_loop(cut, last_index, array, depth_limit);
        last_index = cut;
    }
}

void insertionsort(int first, int last, int* array)
{
    int i, j, temp;
    for (i = first; i < last; i++) {
        j = i;
        temp = array[i];
        while (j != last && temp < array[j - 1]) {
            array[j] = array[j - 1];
            j--;
        }
        array[j] = temp;
    }
    
    return;
}

/* all following function definitions are helper functions */
int int_compare(int a, int b)
{
    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}

int partition(int first_index, int last_index, int median, int* array)
{
    int i = first_index, j = last_index;
    
    for ( ; ; ) {
        
        while (array[i] < median) {
            i++;
        }
        
        j = j - 1;
        
        while (median < array[j]) {
            j = j - 1;
        }
        
        if (i >= j) {
            return i;
        }
        
        swap(array, i, j);
        i++;
        
    }
}

int median(int first, int middle, int last, int* array)
{
    if (array[middle] < array[first]) {
        if (array[last] < array[middle]) {
            return array[middle];
        }
        else {
            if (array[last] < array[first]) {
                return array[last];
            }
            else {
                return array[first];
            }
        }
    }
    else {
        if (array[last] < array[middle]) {
            if (array[last] < array[first]) {
                return array[first];
            }
            else {
                return array[last];
            }
        }
        else {
            return array[middle];
        }
    }
}

void swap(int* array, int first, int second)
{
    int temp = array[first];
    array[first] = array[second];
    array[second] = temp;
}
/************************************************************************************************************************/


