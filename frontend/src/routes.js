import React from "react";
import { Route } from "react-router-dom";
import { Hoc } from "./utility";

import Login from "./components/Login";
import Signup from "./components/Signup";
import HomepageLayout from "./components/Home";

const BaseRouter = () => (
  <Hoc>
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Signup} />
    <Route exact path="/" component={HomepageLayout} />
  </Hoc>
);

export default BaseRouter;
