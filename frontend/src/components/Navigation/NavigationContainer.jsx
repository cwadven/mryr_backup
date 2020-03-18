import React, { useState } from "react";
import NavigationPresenter from "./NavigationPresenter";

export default function NavigationContainer() {
  const [open, setOpen] = useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <NavigationPresenter
      open={open}
      handleOpen={handleOpen}
      handleClose={handleClose}
    />
  );
}
