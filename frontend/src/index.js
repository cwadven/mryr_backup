import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";

import App from "components/App";
import * as serviceWorker from "./serviceWorker";

//Redux Setting
import rootReducer from "store/reducers";
import { createStore } from "redux";
import { Provider } from "react-redux";

//redux debug-Chrome extension
import { composeWithDevTools } from "redux-devtools-extension";

//for middleware
import { applyMiddleware } from "redux";

//Redux Setting End

//Redux Saga Stting
import createSagaMiddleware from "redux-saga";
import rootSaga from "./saga";

const sagaMiddleware = createSagaMiddleware();
//create Store

const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(sagaMiddleware))
);

sagaMiddleware.run(rootSaga);

ReactDOM.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,

  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
