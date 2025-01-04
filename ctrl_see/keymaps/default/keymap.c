#include QMK_KEYBOARD_H


enum layers {
    LAYOUT_EL_ROI,
};

enum combos {
    // letters
    One2_B,
    One4_C,
    One45_D,
    One5_E,
    One24_F,
    One245_G,
    One25_H,
    Two4_I,
    Two45_J,
    One3_K,
    One23_L,
    One34_M,
    One345_N,
    One35_O,
    One234_P,
    One2345_Q,
    One235_R,
    Two34_S,
    Two345_T,
    One36_U,
    One236_V,
    Two456_W,
    One346_X,
    One3456_Y,
    One356_Z,
    
};

// combo definition
const uint16_t PROGMEM one2_combo[] = {KC_A, KC_2, COMBO_END}; // B
const uint16_t PROGMEM one4_combo[] = {KC_A, KC_4, COMBO_END}; // C
const uint16_t PROGMEM one45_combo[] = {KC_A, KC_4, KC_5, COMBO_END}; // D
const uint16_t PROGMEM one5_combo[] = {KC_A, KC_5, COMBO_END}; // E
const uint16_t PROGMEM one24_combo[] = {KC_A, KC_2, KC_4, COMBO_END}; // F
const uint16_t PROGMEM one245_combo[] = {KC_A, KC_2, KC_4, KC_5, COMBO_END}; // G
const uint16_t PROGMEM one25_combo[] = {KC_A, KC_2, KC_5, COMBO_END}; // H
const uint16_t PROGMEM two4_combo[] = {KC_2, KC_4, COMBO_END}; // I
const uint16_t PROGMEM two45_combo[] = {KC_2, KC_4, KC_5, COMBO_END}; // J
const uint16_t PROGMEM one3_combo[] = {KC_A, KC_3, COMBO_END}; // K
const uint16_t PROGMEM one23_combo[] = {KC_A, KC_2, KC_3, COMBO_END}; // L
const uint16_t PROGMEM one34_combo[] = {KC_A, KC_3, KC_4, COMBO_END}; // M
const uint16_t PROGMEM one345_combo[] = {KC_A, KC_3, KC_4, KC_5, COMBO_END}; // N
const uint16_t PROGMEM one35_combo[] = {KC_A, KC_3, KC_5, COMBO_END}; // O
const uint16_t PROGMEM one234_combo[] = {KC_A, KC_2, KC_3, KC_4, COMBO_END}; // P
const uint16_t PROGMEM one2345_combo[] = {KC_A, KC_2, KC_3, KC_4, KC_5, COMBO_END}; // Q
const uint16_t PROGMEM one235_combo[] = {KC_A, KC_2, KC_3, KC_5, COMBO_END}; // R
const uint16_t PROGMEM two34_combo[] = {KC_2, KC_3, KC_4, COMBO_END}; // S
const uint16_t PROGMEM two345_combo[] = {KC_2, KC_3, KC_4, KC_5, COMBO_END}; // T
const uint16_t PROGMEM one36_combo[] = {KC_A, KC_3, KC_6, COMBO_END}; // U
const uint16_t PROGMEM one236_combo[] = {KC_A, KC_2, KC_3, KC_6, COMBO_END}; // V
const uint16_t PROGMEM two456_combo[] = {KC_2, KC_4, KC_5, KC_6, COMBO_END}; // W
const uint16_t PROGMEM one346_combo[] = {KC_A, KC_3, KC_4, KC_6, COMBO_END}; // X
const uint16_t PROGMEM one3456_combo[] = {KC_A, KC_3, KC_4, KC_5, KC_6, COMBO_END}; // Y
const uint16_t PROGMEM one356_combo[] = {KC_A, KC_3, KC_5, KC_6, COMBO_END}; // Z




// list of combos
combo_t key_combos[] = {
    [One2_B] = COMBO(one2_combo, KC_B),
    [One4_C] = COMBO(one4_combo, KC_C),
    [One45_D] = COMBO(one45_combo, KC_D),
    [One5_E] = COMBO(one5_combo, KC_E),
    [One24_F] = COMBO(one24_combo, KC_F),
    [One245_G] = COMBO(one245_combo, KC_G),
    [One25_H] = COMBO(one25_combo, KC_H),
    [Two4_I] = COMBO(two4_combo, KC_I),
    [Two45_J] = COMBO(two45_combo, KC_J),
    [One3_K] = COMBO(one3_combo, KC_K),
    [One23_L] = COMBO(one23_combo, KC_L),
    [One34_M] = COMBO(one34_combo, KC_M),
    [One345_N] = COMBO(one345_combo, KC_N),
    [One35_O] = COMBO(one35_combo, KC_O),
    [One234_P] = COMBO(one234_combo, KC_P),
    [One2345_Q] = COMBO(one2345_combo, KC_Q),
    [One235_R] = COMBO(one235_combo, KC_R),
    [Two34_S] = COMBO(two34_combo, KC_S),
    [Two345_T] = COMBO(two345_combo, KC_T),
    [One36_U] = COMBO(one36_combo, KC_U),
    [One236_V] = COMBO(one236_combo, KC_V),
    [Two456_W] = COMBO(two456_combo, KC_W),
    [One346_X] = COMBO(one346_combo, KC_X),
    [One3456_Y] = COMBO(one3456_combo, KC_Y),
    [One356_Z] = COMBO(one356_combo, KC_Z),

};


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [LAYOUT_EL_ROI] = LAYOUT( KC_A, KC_2, KC_3, KC_4),

};

