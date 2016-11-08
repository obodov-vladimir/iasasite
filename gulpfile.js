/**
 * Created by obodov-vladimir on 24.10.16.
 */
const gulp = require('gulp');
const sourcemaps = require('gulp-sourcemaps');
const less = require('gulp-less');
const concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');

const path = {
    css: 'iasasite/assets/less/*.less',
    js: 'iasasite/assets/js/main.js'
};
const dist = {
    css: 'iasasite/static/css',
    js: 'iasasite/static/js/',
    images: 'iasasite/static/img/',
    fonts: 'iasasite/static/fonts/'
};

gulp.task('default', function() {
  // place code for your default task here
});
gulp.task('styles:dev', function () {
    return gulp.src(path.css)
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(sourcemaps.write())
        // .pipe(concatCss("style.css"))
        .pipe(gulp.dest(dist.css));
});
gulp.task('styles:production', function () {
    return gulp.src(path.css)
        .pipe(less())
        // .pipe(concatCss("style.css"))
        .pipe(cleanCSS())
        .pipe(gulp.dest(dist.css));
});
