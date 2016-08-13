/**
 *  Time Complexity: O(1)
 *  Auxiliary Space Complexity: O(1) 
 **/

function firstTimesLast(array) {
  var result = null;

  if (array.length < 2) {
    return result;
  } else {
    result = array[0] * array[length-1];
    return result;
  }
};

/**
 *  Time Complexity: O(n)
 *  Auxiliary Space Complexity: O(n)
 **/

function mostFrequentOccurrence(string) {
  var lowerString = string.toLowerCase();
  var letters = {};
  var mostFrequent = [];
  
  for(var i = 0; i < lowerString.length; i++) {
    if (letters[lowerString[i]]) {
      letters[lowerString[i]] ++;
    } else {
      letters[lowerString[i]] = 1;
    }
  }

  for(var key in letters) {
    if (!mostFrequent.length) {
      mostFrequent = [key, letters[key]];
    } else {
      if (letters[key] > mostFrequent[1]) {
        mostFrequent = [key, letters[key]];
      }
    }
  }

  return mostFrequent[0];
};

/**
 *  Time Complexity: O(n^2)
 *  Auxiliary Space Complexity: O(1)
 **/

function printUnorderedPairs(array) {
 for (var i = 0; i < array.length; i++) {
    for (var j = i; j < array.length; j++) {
      console.log(array[i] + "," + array[j]);
    }
  }
};

/**
 *  Time Complexity: O(log(n))
 *  Auxiliary Space Complexity: O(log(n))
 **/

function sortedArraySearch(sortedArray, target) {

  var result = false; 

  var hunt = function(start, end){ 
    if (start >= end-1 && (sortedArray[start] === target || sortedArray[end] === target)){
      result = true;
      return;
    } else if (start >= end-1){
      return;
    }

    var mid = Math.floor((start + end) / 2); 

    if (sortedArray[mid] === target){
      result = true;
      return;
    } else if (target > sortedArray[mid]){
      hunt(mid, end);
    } else if (target < sortedArray[mid]){
      hunt(start, mid);
    }

  }

  hunt(0, sortedArray.length-1);
  return result;
};

/**
 *  Time Complexity: O(nm)
 *  Auxiliary Space Complexity: O(mn)
 **/

function makeCombinedMatrix(arrayOne, arrayTwo) {
  var result = []; 
  var row;

  for (var i = 0; i < arrayOne.length; i++) {
    row = [];

    for (var j = 0; j < arrayTwo.length; j++) {
      row.push(arrayTwo[j] + arrayOne[i]);
    }

    result.push(row);
  }

  return result;
};
