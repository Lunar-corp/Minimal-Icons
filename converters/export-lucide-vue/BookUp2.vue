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
    <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2" />
    <path d="M18 2h2v20H6.5a2.5 2.5 0 0 1 0-5H20" />
    <path d="M12 13V7" />
    <path d="m9 10 3-3 3 3" />
    <path d="m9 5 3-3 3 3" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>