import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Grid from '@material-ui/core/Grid';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    logo: {
        width: 150,
        height: 50,
    },
    appbar: {
        boxShadow: 'none',
    },
}));

const Navigation = () => {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);

    return (
        <nav className={classes.root}>
            <AppBar position="static" color="default" className={classes.appbar}>
                <Toolbar>
                    <Grid container justify={"space-between"}>
                        <Grid item xs={2}>
                            <img
                                className={classes.logo}
                                src={"https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"}
                                alt="Placeholder logo"
                            />
                        </Grid>
                        <Grid item xs={5}>
                            <Grid container justify={"flex-end"}>
                                <Tabs
                                    onChange={(e, v) => setValue(v)}
                                    value={value}
                                    aria-label="Navigation-tabs"
                                >
                                    <Tab label={"page 1"} />
                                    <Tab label={"page 2"} />
                                </Tabs>
                            </Grid>
                        </Grid>
                    </Grid>
                </Toolbar>
            </AppBar>
        </nav>
    );
};

export default Navigation;