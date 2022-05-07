import { Knob, Pointer, Value, Arc } from 'rc-knob'

export default function CustomKnob({ initialValue, min, max, disabled, onChange }) {
  return <Knob
    value={initialValue}
    className={`${disabled ? "styledKnob disabled" : "styledKnob"}`}
    size={100}
    angleOffset={220}
    angleRange={280}
    min={min}
    max={max}
    onChange={onChange}
  >
    <Arc
      arcWidth={1.5}
    />
    <circle r="40" cx="50" cy="50" />
    <Pointer
      width={2}
      height={35}
      radius={10}
      type="rect"
      color="#fff"
    />
    <Value
      marginBottom={45}
      className="value"
    />

  </Knob>
}