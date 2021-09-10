import React from "react";
import { TextField, Button, FormControl } from "@material-ui/core";

export default function TodoForm() {
  return (
    <>
      <h1>Please fill out this Form</h1>

      <FormControl>
        <TextField
          id="standard-full-width"
          label="Name"
          style={{ margin: 8 }}
          placeholder=""
          fullWidth
          margin="normal"
          InputLabelProps={{
            shrink: true
          }}
        />

        <TextField
          id="standard-full-width"
          label="Company"
          style={{ margin: 8 }}
          placeholder=""
          fullWidth
          margin="normal"
          InputLabelProps={{
            shrink: true
          }}
        />

        <TextField
          id="standard-full-width"
          label="Email address"
          style={{ margin: 8 }}
          placeholder=""
          fullWidth
          margin="normal"
          InputLabelProps={{
            shrink: true
          }}
        />

        <br />
        <br />
        <Button variant="contained" color="primary">
          Submit
        </Button>
      </FormControl>
    </>
  );
}
