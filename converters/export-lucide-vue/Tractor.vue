<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m10 11 11 .9c.6 0 .9.5.8 1.1l-.8 5h-1" />
    <path d="M16 18h-5" />
    <path d="M18 5a1 1 0 0 0-1 1v5.573" />
    <path d="M3 4h9l1 7.246" />
    <path d="M4 11V4" />
    <path d="M7 15h.01" />
    <path d="M8 10.1V4" />
    <circle cx="18" cy="18" r="2" />
    <circle cx="7" cy="15" r="5" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>