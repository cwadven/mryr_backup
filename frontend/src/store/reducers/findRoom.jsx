import * as actionTypes from "../actions/actionTypes";

const initialState = {};

const test = (state, action) => {
  return { ...state };
};

const findRoom = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.TEST:
      return test(state, action);

    default:
      return state;
  }
};

export default findRoom;
