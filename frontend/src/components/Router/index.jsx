import React from "react";
import { Router, Route, Redirect, Switch } from "react-router-dom";
import { createBrowserHistory as createHistory } from "history";
import FindRoom from "routes/FindRoom";
import PutOutRoom from "routes/PutOutRoom";

const history = createHistory();

export default function Routes() {
  let route = null;

  route = (
    <Switch>
      <Route exact path="/" component={FindRoom} />
      <Route path="/putout" component={PutOutRoom} />
      <Redirect from="*" to="/" />
    </Switch>
  );

  return <Router history={history}>{route}</Router>;
}
